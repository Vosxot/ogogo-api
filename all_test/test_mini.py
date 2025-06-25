import os
import pytest

def test_verify_otp_success(session, config):
    """
    Успешная проверка валидного OTP.
    (этот эндпоинт принимает form-data)
    """
    url  = f"{config['base_url']}/Clients/VerifyOtpForLoginByPhone"
    form = {"phone": config["phone"], "otp": config["otp"]}
    resp = session.post(url, data=form)
    print("➡️ Ответ VerifyOtp:", resp.text)
    assert resp.status_code == 200, resp.text

    # в ответе result — это строка с sessionId
    token = resp.json().get("result")
    assert isinstance(token, str) and token, "Не получили sessionId"
    config["sessionId"] = token


def test_login_by_phone(session, config):
    """
    Логинимся по телефону + sessionId с селфи на LoginByPhone.
    """
    assert "sessionId" in config, "Нет sessionId — предыдущий тест не прошёл"
    url = f"{config['base_url']}/Clients/LoginByPhone"
    data = {
        "phone": config["phone"],
        "token": config["sessionId"]
    }
    selfie = config.get("selfie_path", "files/selfie.jpg")
    assert os.path.exists(selfie), f"Селфи не найдено: {selfie}"
    with open(selfie, "rb") as f:
        files = {"file": (os.path.basename(selfie), f, "image/jpeg")}
        resp = session.post(url, data=data, files=files)
    print("➡️ Ответ LoginByPhone:", resp.text)
    assert resp.status_code == 200, resp.text


@pytest.mark.parametrize("otp_value, expected", [
    ("9999", [400, 401]),  # неверный код
    ("",    400),          # пустой
])
def test_verify_otp_negative(session, config, otp_value, expected):
    """
    Негативные сценарии для VerifyOtpForLoginByPhone.
    """
    url = f"{config['base_url']}/Clients/VerifyOtpForLoginByPhone"
    resp = session.post(url, data={"phone": config["phone"], "otp": otp_value})
    print(f"➡️ VerifyOtpBad({otp_value}):", resp.text)
    if isinstance(expected, list):
        assert resp.status_code in expected
    else:
        assert resp.status_code == expected
