# Write a function difference_sets that takes two sets and returns the difference
# of the first set minus the second set. Illustrate this with an example where
# you have a set of attendees who registered for an event and a set of attendees
#  who actually attended. Find out who registered but did not attend.

def difference_sets(set1,set2):
            not_attend=set1.difference(set2)
            return not_attend
    # try:
    #     if isinstance(set1,set) and isinstance(set2,set):
    #     else:
    #         raise TypeError("not a set")
    # except Exception as e:
    #     print(f"error {e}")
    # finally:
    #     print("execution are completed")

set3={"Adil","Sial","Talha","huraira","Arslan","Imran"}
set4={"Adil","Talha","huraira"}
print(difference_sets(set3,set4))


