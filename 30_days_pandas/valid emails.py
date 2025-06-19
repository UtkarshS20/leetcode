import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # condition = (users["mail"].str[0].apply(str.isalpha) &
    #     (users["mail"].str.split("@").str[-1] == 'leetcode.com') &
    # ((users["mail"].str.split("@").str[0].str.contains('-', regex=False) |
    # users["mail"].str.split("@").str[0].str.contains('_', regex=False) |
    # users["mail"].str.split("@").str[0].str.contains('.', regex=False)) |
    # users["mail"].str.split("@").str[0].apply(str.isalnum)  )  
    # )
    # users.loc[condition,"valid_mail"] = users.loc[condition, "mail"]
    # users["mail"] = users["valid_mail"]
    # users.drop(columns=["valid_mail"], inplace=True)
    # users = users.dropna(subset=["mail"])

    # return users
    def is_valid_email(email: str) -> bool:
        # 1. Check if email ends with @leetcode.com
        if not email.endswith('@leetcode.com'):
            return False
        
        # 2. Split the email into prefix and domain
        parts = email.split('@')
        if len(parts) != 2:
            return False
        prefix = parts[0]
        
        # 3. Prefix must not be empty and must start with a letter
        if not prefix or not prefix[0].isalpha():
            return False
        
        # 4. All characters must be letters, digits, _, ., or -
        for char in prefix:
            if not (char.isalnum() or char in {'_', '.', '-'}):
                return False
        
        return True
    
    # Apply the validation function to each row
    valid_mask = users['mail'].apply(is_valid_email)
    
    return users[valid_mask]

users = pd.DataFrame([[1, "Winston", "winston@leetcode.com"], 
[2, "Jonathan", "jonathanisgreat"], 
[3, "Annabelle", "bella-@leetcode.com"], 
[4, "Sally", "sally.come@leetcode.com"], 
[5, "Marwan", "quarz#2020@leetcode.com"], 
[6, "David", "david69@gmail.com"], 
[7, "Shapiro", ".shapo@leetcode.com"]],
columns=["user_id", "name", "mail"])

print(valid_emails(users=users))