import csv
import analytics
analytics.write_key = 'yREWPN5Nl4t7m3onA8ZJ8pE32S2SGfhH'
analytics.host = 'events.eu1.segmentapis.com/v1/'
data = []
rowCount = 0
with open('data/Sample_Track.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        data.append(row)
        if rowCount > 0:
            analytics.track(data[rowCount][1], data[rowCount][3], {
                'email': data[rowCount][4],
                'first_name': data[rowCount][5],
                'last_name': data[rowCount][6],
                'city': data[rowCount][7],
                'country': data[rowCount][8],
                'postal_code': data[rowCount][9],
                'street': data[rowCount][10],
                'gender': data[rowCount][11],
                'phone': data[rowCount][12],
                'coupon_code': data[rowCount][13],
                'currency': data[rowCount][14],
                'order_id': data[rowCount][15],
                'payment_method': data[rowCount][16],
                'product_category': data[rowCount][17],
                'product_name': data[rowCount][18],
                'price': data[rowCount][19],
                'product_id': data[rowCount][20],
                'quantity': data[rowCount][21],
                'revenue': data[rowCount][22],
                'shipping': data[rowCount][23],
                'tax': data[rowCount][24],
                'value': data[rowCount][25],
                'order_status': data[rowCount][26],
                'discount_amount': data[rowCount][27]
            })
        rowCount = rowCount+1
