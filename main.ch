# This is a very useful piece of software

FUN oopify(prefix) -> prefix + "oop"

FUN join(elements, separator)
	VAR result = ""
	VAR len = len(elements)

	FOR i = 0 TO len THEN
		VAR result = result + elements/i
		IF i != len - 1 THEN VAR result = result + separator
	END

	RETURN result
END

FUN map(elements, func)
	VAR new_elements = []

	FOR i = 0 TO len(elements) THEN
		APPEND(new_elements, func(elements/i))
	END

	RETURN new_elements
END

print("Greetings universe!")

FOR i = 0 TO 5 THEN
	print(join(map(["l", "sp"], oopify), ", "))

END
