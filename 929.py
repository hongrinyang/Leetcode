class Solution:
    def numUniqueEmails(self, emails):
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            # Remove dots from the local name
            local = local.replace('.', '')
            
            # Only take the part before the first '+'
            if '+' in local:
                local = local.split('+')[0]
            
            # Reconstruct the email and add it to the set
            unique_emails.add(local + '@' + domain)
        
        # The number of unique emails is the size of the set
        return len(unique_emails)
