# Orders Db. Here each record is in the format [epoch_timestamp, order_id, price]
Orders_db = [[1347517405, 54413, '78'], [1347517413, 54421, '86'], [1347517454, 54462, '127'], [1347517460, 54468, '133'], [1347517461, 54469, '134'], [1347517426, 54434, '99'], [1347517464, 54472, '137'], [1347517394, 54402, '67'], [1347517445, 54453, '118'], [1347517375, 54383, '48'], [1347517377, 54385, '50'], [1347517392, 54400, '65'], [1347517450, 54458, '123'], [1347517404, 54412, '77'], [1347517389, 54397, '62'], [1347517393, 54401, '66'], [1347517440, 54448, '113'], [1347517457, 54465, '130'], [1347517444, 54452, '117'], [1347517400, 54408, '73'], [1347517412, 54420, '85'], [1347517371, 54379, '44'], [1347517415, 54423, '88'], [1347517441, 54449, '114'], [1347517435, 54443, '108'], [1347517409, 54417, '82'], [1347517398, 54406, '71'], [1347517422, 54430, '95'], [1347517468, 54476, '141'], [1347517402, 54410, '75'], [1347517437, 54445, '110'], [1347517446, 54454, '119'], [1347517382, 54390, '55'], [1347517399, 54407, '72'], [1347517438, 54446, '111'], [1347517416, 54424, '89'], [1347517380, 54388, '53'], [1347517425, 54433, '98'], [1347517406, 54414, '79'], [1347517449, 54457, '122'], [1347517388, 54396, '61'], [1347517430, 54438, '103'], [1347517455, 54463, '128'], [1347517458, 54466, '131'], [1347517452, 54460, '125'], [1347517396, 54404, '69'], [1347517423, 54431, '96'], [1347517465, 54473, '138'], [1347517397, 54405, '70'], [1347517459, 54467, '132'], [1347517395, 54403, '68'], [1347517381, 54389, '54'], [1347517424, 54432, '97'], [1347517436, 54444, '109'], [1347517434, 54442, '107'], [1347517401, 54409, '74'], [1347517376, 54384, '49'], [1347517467, 54475, '140'], [1347517456, 54464, '129'], [1347517427, 54435, '100'], [1347517383, 54391, '56'], [1347517451, 54459, '124'], [1347517433, 54441, '106'], [1347517414, 54422, '87'], [1347517417, 54425, '90'], [1347517453, 54461, '126'], [1347517378, 54386, '51'], [1347517432, 54440, '105'], [1347517403, 54411, '76'], [1347517439, 54447, '112'], [1347517448, 54456, '121'], [1347517410, 54418, '83'], [1347517391, 54399, '64'], [1347517447, 54455, '120'], [1347517421, 54429, '94'], [1347517379, 54387, '52'], [1347517411, 54419, '84'], [1347517386, 54394, '59'], [1347517384, 54392, '57'], [1347517374, 54382, '47'], [1347517462, 54470, '135'], [1347517431, 54439, '104'], [1347517419, 54427, '92'], [1347517428, 54436, '101'], [1347517466, 54474, '139'], [1347517443, 54451, '116'], [1347517463, 54471, '136'], [1347517385, 54393, '58'], [1347517387, 54395, '60'], [1347517373, 54381, '46'], [1347517372, 54380, '45'], [1347517418, 54426, '91'], [1347517420, 54428, '93'], [1347517469, 54477, '142]'], [1347517442, 54450, '115'], [1347517408, 54416, '81'], [1347517390, 54398, '63'], [1347517407, 54415, '80'], [1347517429, 54437, '102']]

# This method should sort the orders db on epoch_timestamp
# This is a standard merge sort implementation with one minor addition. look for ** below
def merge_sort_orders(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort_orders(L)  # Sorting the first half
        merge_sort_orders(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        # The Merge step
        while i < len(L) and j < len(R):
            # ** following is the only condition which needs to be modified in a standard merge sort to make it handle nested lists.
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Standard binary search implementation with one minor edit. look for ** below
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        mid_date = arr[mid]

        # ** This is the only edit in the condition to handle nested lists.
        if int(x) == int(mid_date[0]):
            return mid_date

        # Check if x is present at mid
        elif int(mid_date[0]) < int(x):
            low = mid + 1

        # If x is greater, ignore left half
        elif int(mid_date[0]) > int(x):
            high = mid - 1

    # If we reach here, then the element was not present
    return False


if __name__ == '__main__':
    print("Orders Db before sorting:")
    print(Orders_db)

    # Sorting the db based on 0th value
    merge_sort_orders(Orders_db)
    print("Orders Db after sorting:")
    print(Orders_db)


    ## Searching for a record using timestamp epoch
    print("Searched Record")
    print(binary_search(Orders_db,1347517461))