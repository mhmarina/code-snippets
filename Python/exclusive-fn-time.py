class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # struct: [parent_index, index, start time]
        # first element parent index = -1
        call_stack = []
        result = [0 for i in range(n)] # initialize all vals in list with 0

        # push first element to stack
        vals = logs[0].split(':')
        call_stack.append([int(vals[0]), int(vals[2])])

        i = 1
        while i < len(logs):
            #if I read end I can just pop
            # I dont need to check the elements
            vals = logs[i].split(':')
            curr_index = int(vals[0])
            time_val = int(vals[2])

            if vals[1] == 'start':
                call_stack.append([curr_index, time_val])

            if vals[1] == 'end':
                time = 1
                # check if parent and callee are equal
                if(call_stack):
                    popped = call_stack.pop(-1)
                    time_start = popped[1]
                    time += time_val - time_start
                result[curr_index] += time
                # subtract from parent ...
                if(call_stack):
                    result[call_stack[-1][0]] -= time
            i += 1

        return result