from flask import Flask, render_template, request
import pickle
import numpy as np

# define

flask_app = Flask(__name__, template_folder='templates')

input_names = ['no_of_adults',
               'no_of_children',
               'no_of_weekend_nights',
               'no_of_week_nights',
               'type_of_meal_plan',
               'required_car_parking_space',
               'room_type_reserved',
               'lead_time',
               'arrival_year',
               'arrival_month',
               'arrival_date',
               'market_segment_type',
               'repeated_guest',
               'no_of_previous_cancellations',
               'no_of_previous_bookings_not_canceled',
               'avg_price_per_room',
               'no_of_special_requests',
               ]

cat_features = ['type_of_meal_plan',
                'room_type_reserved',
                'market_segment_type',
                ]

model = pickle.load(open(r'NoteBooks\model.pkl', 'rb'))


@flask_app.route('/')
def home():
    return render_template('home.html')


@flask_app.route('/predict', methods=['POST'])
def predict():
    features = []
    for col in input_names:
        value = request.form.get(col)

        if col in cat_features:
            le = pickle.load(open(r'NoteBooks\{}_le.pkl'.format(col), 'rb'))
            v = le.transform(np.array([[value]]))
            features.append(v)
        else:
            features.append(float(value))
    X = np.array(features).reshape(1, 17)
    y_pred = model.predict(X)

    output =''
    if y_pred == 1:
        output = 'The Customer may confirm the Reservation'
    else:
        output = 'The Customer may not confirm the Reservation'
    return render_template('result.html', prediction_text=output)


if __name__ == '__main__':
    flask_app.run()
