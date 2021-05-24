def email_validator(email) -> bool:
    pattern = r"^(\w*)+([\.\+]\w+)*@(((\w+)\.)+(\w{2,3})$)|(\[\d[12]?\d{1,2}(\.\d[12]?\d{1,2}){3}\])"
