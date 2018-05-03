Rest API Usage

    This api can used according to functionality you have requested

    GET http://<url>/ifsc?ifsc=<ifsc code>: For getting bank details
    GET http://<url>/ifsc?page=<page no>:get ifsc codes with banks

    GET http://<url>/<bank name>?page=<page no>:get ifsc codes of the bank
    GET http://<url>/<bank name>?city=<city>: For all branches for bank in the city

API details

    This is api was created with Flask and mongodb.
    The reason for choosing mongo is because of
    fast querying of documents and storing of data,
    the database is hosted at mlab and application is
    hosted at heroku