FROM mongo

COPY client_portfolio.json /client_portfolio.json

CMD mongoimport mongodb://client_portfolio:27017 --db=portfolio --collection=client_portfolio --jsonArray --file=/client_portfolio.json --port 27017