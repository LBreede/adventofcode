DAY = 99
FILE_NAME = format('../day%02d_input.txt', DAY)
EXAMPLE = ''

def part_one(input)
  # impl
end

def part_two(input)
  # impl
end

puts format('Advent of Code 2025 - Day %02d', DAY)

puts "\n--- Part One ---"
raise 'part_one example failed!' unless part_one(EXAMPLE) == -1

input = File.read(File.expand_path(FILE_NAME, __FILE__))
start = Time.now
result = part_one(input)
elapsed = Time.now - start
puts "Result = #{result} (took #{elapsed.round(6)}s)"

puts "\n--- Part Two ---"
raise 'part_two example failed!' unless part_two(EXAMPLE) == -1

start = Time.now
result = part_two(input)
elapsed = Time.now - start
puts "Result = #{result} (took #{elapsed.round(6)}s)"
