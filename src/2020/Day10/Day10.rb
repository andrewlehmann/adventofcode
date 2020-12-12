def buildData(filename)
  input = File.readlines(filename).map { |line| line.to_i }.sort
  input << input.max + 3
  input.unshift(0)

  input
end

joltages = buildData('input.txt')

# PART 1
joltageDiffs = joltages.each_cons(2).map { |a,b| b-a}
joltageDiffsMap = Hash[joltageDiffs.uniq.map { |e| [e, joltageDiffs.count(e)] }]

result = joltageDiffsMap[1] * joltageDiffsMap[3]

puts result 


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

  numOfPaths
end

possiblePaths = Hash[joltages.map { |e| [e, joltages.select { |f| f - e <= 3 and f - e > 0 }] }]

# Do DFS to find all possible paths
visitedNodes = Hash[joltages.map {|e| [e, false] }]
result2 = checkNode(possiblePaths, 0, joltages.max, visitedNodes)

puts result2