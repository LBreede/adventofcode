# frozen_string_literal: true

def invalid1?(id)
  id_s = id.to_s
  return false if id_s.length.odd?

  half = id_s.length / 2
  id_s[0...half] == id_s[half..]
end

def part_one(input)
  input.split(',').sum do |range|
    first, last = range.split('-', 2).map(&:to_i)
    (first..last).select { |id| invalid1?(id) }.sum
  end
end

def invalid2?(id)
  s = id.to_s
  len = s.length

  (1..len / 2).each do |x|
    next unless (len % x).zero?

    pattern = s[0, x]
    times = len / x
    return true if (1..times - 1).all? { |i| s[i * x, x] == pattern }
  end

  false
end

def part_two(input)
  input.split(',').sum do |range|
    first, last = range.split('-', 2).map(&:to_i)
    (first..last).select { |id| invalid2?(id) }.sum
  end
end

example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"

DAY = 2
FILE_NAME = format('../day%02d_input.txt', DAY)

puts format('Advent of Code 2025 - Day %02d', DAY)

puts "\n--- Part One ---"
raise 'part_one example failed!' unless part_one(example) == 1_227_775_554

input = File.read(File.expand_path(FILE_NAME, __FILE__))
start = Time.now
result = part_one(input)
elapsed = Time.now - start
puts "Result = #{result} (took #{elapsed}s)"

puts "\n--- Part Two ---"
raise 'part_two example failed!' unless part_two(example) == 4_174_379_265

start = Time.now
result = part_two(input)
elapsed = Time.now - start
puts "Result = #{result} (took #{elapsed}s)"
