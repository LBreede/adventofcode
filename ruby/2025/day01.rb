# frozen_string_literal: true

def op_for(line)
  case line[0]
  when 'L' then ->(n, d) { (n - d) % 100 }
  when 'R' then ->(n, d) { (n + d) % 100 }
  end
end

def part_one(input)
  dial = 50
  password = 0
  input.each_line do |line|
    line = line.strip
    next if line.empty?

    op = op_for(line)
    next unless op

    dial = op.call(dial, line[1..].to_i)
    password += 1 if dial.zero?
  end
  password
end

def part_two(input)
  dial = 50
  password = 0

  input.each_line do |line|
    line = line.strip
    next if line.empty?

    op = op_for(line)
    next unless op

    line[1..].to_i.times do
      dial = op.call(dial, 1)
      password += 1 if dial.zero?
    end
  end
  password
end

example = <<~TEXT
  L68
  L30
  R48
  L5
  R60
  L55
  L1
  L99
  R14
  L82
TEXT

DAY = 1
FILE_NAME = format('../day%02d_input.txt', DAY)

puts format('Advent of Code 2025 - Day %02d', DAY)

puts "\n--- Part One ---"
raise 'part_one example failed!' unless part_one(example) == 3

input = File.read(File.expand_path(FILE_NAME, __FILE__))
start = Time.now
result = part_one(input)
elapsed = Time.now - start
puts "Result = #{result} (took #{elapsed}s)"

puts "\n--- Part Two ---"
raise 'part_two example failed!' unless part_two(example) == 6

start = Time.now
result = part_two(input)
elapsed = Time.now - start
puts "Result = #{result} (took #{elapsed}s)"
