# frozen_string_literal: true

DAY = 3
FILE_NAME = format('../day%02d_input.txt', DAY)
EXAMPLE = <<~TEXT
  987654321111111
  811111111111119
  234234234234278
  818181911112111
TEXT

def max_k_subseq(digits, k)
  puts "digits.length = #{digits.length}"
  puts "k = #{k}"
  to_remove = digits.length - k
  puts "to_remove = #{to_remove}"
  stack = []

  digits.each do |d|
    while to_remove.positive? && !stack.empty? && stack.last < d
      stack.pop
      to_remove -= 1
    end
    stack << d
    puts "stack = #{stack}"
  end

  stack.take(k).join.to_i
end

def solve(input, k:)
  input.each_line.sum do |line|
    digits = line.chomp.scan(/\d/) # keep only digits
    next 0 if digits.length < k

    max_k_subseq(digits, k)
  end
end

def part_one(input)
  solve(input, k:  2)
end

def part_two(input)
  solve(input, k: 12)
end

test = max_k_subseq('818181911112111'.chomp.scan(/\d/), 3)
puts test

# puts format('Advent of Code 2025 - Day %02d', DAY)
#
# puts "\n--- Part One ---"
# raise 'part_one example failed!' unless part_one(EXAMPLE) == 357
#
# input = File.read(File.expand_path(FILE_NAME, __FILE__))
# start = Time.now
# result = part_one(input)
# elapsed = Time.now - start
# puts "Result = #{result} (took #{elapsed.round(6)}s)"
#
# puts "\n--- Part Two ---"
# raise 'part_two example failed!' unless part_two(EXAMPLE) == 3_121_910_778_619
#
# start = Time.now
# result = part_two(input)
# elapsed = Time.now - start
# puts "Result = #{result} (took #{elapsed.round(6)}s)"
