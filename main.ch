~ This is a very useful piece of software

func oopify(prefix) -> prefix + "oop"

func join(elements, separator)
	let result = ""
	let len = len(elements)

	for i = 0 to len then
		let result = result + elements/i
		if i != len - 1 then let result = result + separator
	end
~ this is a comment
	return result
end

func map(elements, myFunc)
	let new_elements = []

	for i = 0 to len(elements) then
		append(new_elements, myFunc(elements/i))
	end

	return new_elements
end

print("Matthew")
print("Greetings universe!")

for i = 0 to 5 then
	print(join(map(["l", "sp"], oopify), ", "))
end

print("Done")
