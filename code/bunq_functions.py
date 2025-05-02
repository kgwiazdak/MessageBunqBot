from bunq.sdk.context.api_context import ApiContext
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.generated.object_ import AmountObject, PointerObject
from bunq.sdk.model.generated.endpoint import PaymentApiObject, MonetaryAccountBankApiObject, RequestInquiryApiObject
from bunq import Pagination
from bunq import ApiEnvironmentType


api_context = ApiContext.create(
    ApiEnvironmentType.SANDBOX,
    "XYZ",
    "Kontekst z kartki"
)
api_context.save("bunq_api_context_kartka.conf")
BunqContext.load_api_context(api_context)

user_context = BunqContext.user_context()
acc_list = MonetaryAccountBankApiObject.list()
user_context._primary_monetary_account = acc_list.value[1]


def get_last_transactions(limit: int = 5):
    pagination = Pagination()
    pagination.count = limit

    acc_list = MonetaryAccountBankApiObject.list()
    for acc in acc_list.value:
        if float(acc.balance.value) > 0:
            selected_account = acc
            break

    transactions = PaymentApiObject.list(
        params=pagination.url_params_count_only,
        monetary_account_id=selected_account.id_).value

    response_lines = ["Your last transactions:"]
    for payment in transactions:
        amount = payment.amount.value
        currency = payment.amount.currency
        description = payment.description or "No description"
        date = payment.created.split("T")[0]
        response_lines.append(f"- {date}: {amount} {currency} ({description})")

    return "\n".join(response_lines)


def pay(receiver_alias_name: str, receiver_alias_value: str, amount: float, description: str = "Payment") -> None:
    """
    Instant transaction.
    e.g. pay("PHONE_NUMBER", "+31613127783", 7.5, 'second payment')
    """
    payment_id = PaymentApiObject.create(
        amount=AmountObject(f"{amount}", "EUR"),
        counterparty_alias=PointerObject(receiver_alias_name, receiver_alias_value),
        description=description
    ).value

    return f'Payment successfull with id: {payment_id}'

def request_payment(receiver_alias_name: str, receiver_alias_value: str, amount: float, description: str = "Payment request") -> None:
    """
    Payment request.
    e.g. request_payment("PHONE_NUMBER", "+31613127783", 6.5, 'Little payment request`')
    """
    request_id = RequestInquiryApiObject.create(
        AmountObject(f"{amount}", "EUR"),
        PointerObject(receiver_alias_name, receiver_alias_value),
        description,
        allow_bunqme=False
    ).value

    return f'Payment request successfull with id: {request_id}'

def request_mult_payments(payment_details: dict):
    for receiver_alias, amount in payment_details.items():
        request_payment("PHONE_NUMBER", receiver_alias, amount)
