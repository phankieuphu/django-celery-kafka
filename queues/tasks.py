from __future__ import absolute_import
from .celerys import app
import time


@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
    return x + y


@app.task
def updateTopStore(old_value, new_value):
    # Assume stores is a list of store objects with fields: top_store, point, interactivity

    # Sort stores by interactivity and point in descending order
    sorted_stores = sorted(stores, key=lambda x: (
        x.interactivity, x.point), reverse=True)

    # Find index of store to update
    store_to_update = next(
        (s for s in sorted_stores if s.top_store == old_value), None)
    if store_to_update is None:
        # Handle case where store with old_value not found
        return

    update_index = sorted_stores.index(store_to_update)

    # Update top_store field and increment values for higher indices
    for i in range(update_index, len(sorted_stores)):
        sorted_stores[i].top_store += 1

    # Update store object in original list
    stores[update_index].top_store = new_value
