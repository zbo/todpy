__author__ = 'ian.zhang'

import ldap
import pdb

conn = ldap.initialize('ldap://10.32.51.55')
_username = u'ian.zhang@rcoffice.ringcentral.com'
_dn = 'CN=GIT SJC Service,OU=Service Accounts,OU=RingCentral,DC=rcoffice,DC=ringcentral,DC=com'
_password = '7a$GLCq0810d2x'
conn.bind_s(_dn, _password)

pdb.set_trace()
result_id = conn.search('DC=rcoffice,DC=ringcentral,DC=com',ldap.SCOPE_SUBTREE, "(|(|(SAMAccountName=%(user)s)(distinguishedName=%(user)s))(userPrincipalName=%(user)s))"%{"user":_username})

result = conn.result(msgid=result_id, all=0, timeout=10)
print result
