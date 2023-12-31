from fastapi import FastAPI
from routes.index import router, Userrouter, Applicationrouter, BankAccountRouter, LoanPaymentRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Allow all origins (not recommended for production, use a list of allowed origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping')
def test_route():
    return {"msg": "pong"}

prefix = "/api/v1"

app.include_router(router, prefix=prefix+"/tests", tags=["tests"])
app.include_router(Userrouter, prefix=prefix+"/users", tags=["Users"])
app.include_router(Applicationrouter, prefix=prefix+"/applications", tags=["Applications"])
app.include_router(BankAccountRouter, prefix=prefix+"/bank_accounts", tags=["Bank Accounts"])
app.include_router(LoanPaymentRouter, prefix=prefix+"/loan_payments", tags=["Loan Payments"])