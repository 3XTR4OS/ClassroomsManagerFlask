from classrooms_app import cabs_app
from flask import render_template, redirect, url_for, jsonify
from .models import Cabinet, Reservations, db
from flask import request


@cabs_app.route('/cab-process', methods=['GET', 'POST'])
def cab_process():
    """Обрабатывает пришедшие данные с сайта, управляет шаблонами"""
    filters = request.get_json()  # data from request
    print(filters)
    form_filters = {}
    only_occupied: bool = False

    selected_pair: str | int = filters.get('selected_pair')

    # Если пара выбрана
    if selected_pair.isdigit():
        selected_pair = int(selected_pair)
    else:
        return render_template('gen_table_body.html', cabinets=[])

    # То начинаем собирать фильтры запроса
    if filters.get('cab_is_gym'):
        form_filters['cab_is_gym'] = True

    if filters.get('cab_with_projector'):
        form_filters['cab_with_projector'] = True

    if filters.get('cab_is_small'):
        form_filters['cab_is_small'] = True

    if filters.get('cab_is_computer'):
        form_filters['cab_is_computer'] = True

    if filters.get('is_occupied') == 'true':
        only_occupied = True

    cabinets_query = Cabinet.query.filter_by(**form_filters).order_by(Cabinet.cab_number)

    if only_occupied:
        # Занятый кабинет -> кабинет в таблице Reservations
        occupied_cabs = (
            cabinets_query
            .join(Reservations, Cabinet.cab_number == Reservations.cab_number)
            .filter(Reservations.pair_number == selected_pair)
            .order_by(Cabinet.cab_number)
            .all()
        )

        return render_template('gen_table_body_occupied.html', cabinets=occupied_cabs)

    else:
        # Свободный кабинет -> кабинет вне таблицы Reservations
        occupied_cab_numbers = db.session.query(Reservations.cab_number).filter(
            Reservations.pair_number == selected_pair).subquery()
        free_cabs = cabinets_query.filter(Cabinet.cab_number.notin_(occupied_cab_numbers))
        free_cabs = free_cabs.order_by(Cabinet.cab_number).all()

        return render_template('gen_table_body.html', cabinets=free_cabs)


@cabs_app.route('/', methods=['GET', 'POST'])
def ajax_test():
    return render_template('ajax_test.html', cabinets=Cabinet.query.all())


@cabs_app.route('/occupy_cabinet', methods=['POST'])
def occupy_cabinet():
    req_data: dict[str] = request.get_json()  # Получаем данные из запроса
    selected_pair = int(req_data.get('selected_pair'))
    cabinet_number: int = int(req_data.get('cab_number'))

    new_reservation = Reservations(cab_number=cabinet_number, pair_number=selected_pair)
    db.session.add(new_reservation)
    db.session.commit()

    return jsonify({'status': 'success'}), 200  # Возвращаем успешный ответ

@cabs_app.route('/make_free_cabinet', methods=['POST'])
def make_free_cabinet():
    req_data: dict[str] = request.get_json()  # Получаем данные из запроса
    cab_number: int = int(req_data.get('cab_number'))
    selected_pair: int = int(req_data.get('selected_pair'))

    reservation_query = db.session.query(Reservations).filter(
        Reservations.cab_number == cab_number,
        Reservations.pair_number == int(selected_pair)
    ).delete()
    db.session.commit()

    return jsonify({'status': 'success'}), 200


@cabs_app.route('/delete_all_reservations', methods=['POST'])
def delete_all_reservations():
    try:
        db.session.query(Reservations).delete()
        db.session.commit()  # Фиксируем изменения в базе данных
        return jsonify({'status': 'success', 'message': 'Все зарезервированные кабинеты очищены'}), 200

    except Exception as e:
        db.session.rollback()  # Откатываем изменения в случае ошибки
        return jsonify({'status': 'error', 'message': str(e)}), 500