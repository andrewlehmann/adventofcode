# PART 1
def getJoltageDiffs(joltages)
  joltages.each_cons(2).map { |a,b| b-a}
end


def buildData(filename)
  input = File.readlines(filename).map { |line| line.to_i }.sort
  input << input.max + 3
  input.unshift(0)

  input
end

data = buildData('input.txt')
diffs = getJoltageDiffs(data)

diffsMap = Hash[diffs.uniq.map { |e| [e, diffs.count(e)] }]

result = diffsMap[1] * diffsMap[3]

# puts result 


# PART 2

def checkNode(graph, node, destination, visited, numOfPaths = 0, memo = {})
  visited[node] = true;
  if node == destination
    numOfPaths += 1
  elsif memo.has_key?(node)
    numOfPaths += memo[node]
  else
    for num in graph[node] do
      if !visited[num]
        numOfPaths = numOfPaths + checkNode(graph, num, destination, visited, 0, memo)
      end
    end
  end

  visited[node] = false
  memo[node] = numOfPaths
  return numOfPaths
end

# Build list of edges in graph
visitedNodes = Hash[data.map {|e| [e, false] }]

possiblePaths = {}
data.each { |e| possiblePaths[e] = data.select { |f| f - e <= 3 and f - e > 0 }.map {|f| f}}

result2 = checkNode(possiblePaths, 0, data.max, visitedNodes)
puts result2
# Do DFS to find all possible paths