# Define a function filter_kwargs that accepts any number of keyword arguments
# and filters out those whose values are integers. Print the filtered values and
# keywords in form of list of tuples i.e. [(key1, val1), (key2, val2)], etc.

def filter_kwargs(**kwargs):
    filtered=[]
    for key,val in kwargs.items():
        if isinstance(val,int):
            filtered.append((key,val))
    print(filtered)

filter_kwargs(name="Adil",age=24,city="Hafizabad",score=100)








# def filter_kwargs(**kwargs):
#     filtered=[]
#     for key,val in kwargs.items():
#         if isinstance(val, int):
#             filtered.append((key,val))
#     print(filtered)

# filter_kwargs(name='Adil Sial', age=24, city='Hafizabad',score=95)
