def set_seed(seed):
    import random
    import factory.random
    from faker import Faker
    random.seed(seed)
    factory.random.reseed_random(seed)
    fake = Faker()  # noqa
    Faker.seed(seed)
