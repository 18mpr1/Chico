# This is a very useful piece of software

FUN oopify(prefix) -> prefix + "oop"

FUN join(elements, separator)
	let result = ""
	let len = len(elements)

	for i = 0 TO len then
		let result = result + elements/i
		if i != len - 1 then let result = result + separator
	end

	return result
end

FUN map(elements, func)
	let new_elements = []

	for i = 0 TO len(elements) then
		append(new_elements, func(elements/i))
	end

	return new_elements
end

print("Greetings universe!")

for i = 0 TO 5 then
	print(join(map(["l", "sp"], oopify), ", "))

end