import yaml

config = None

with open('config.yml', 'r') as config_file:
    try:
        config = yaml.safe_load(config_file)
    except yaml.YAMLError as err:
        print(err)
        exit(1)

if config is None:
    print('Error with the config')
    exit(1)
elif 'sms_gateway' not in config:
    print('You need the sms_gateway')
    exit(1)
elif 'email' not in config:
    print('You need the email')
    exit(1)
elif 'password' not in config:
    print('You need the password')
    exit(1)
elif 'number' not in config:
    print('You need the phone number')
    exit(1)
elif 'term' not in config:
    print('You need the term')
    exit(1)
elif 'courses' not in config:
    print('You need the courses')
    exit(1)