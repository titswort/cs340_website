from app import app, db
from app.models import Mutual_Funds, Stocks, User, Portfolios, Sectors, Holdings

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Portfolios': Portfolios, 'Mutual_Funds': Mutual_Funds, 'Stocks': Stocks, 'Sectors': Sectors, 'Holdings': Holdings}

if __name__ == '__main__':
    app.run(host='flip2.engr.oregonstate.edu', port=12323, use_reloader=True, debug=False)
