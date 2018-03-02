module Model
  class Author
    def initialize(firstname, lastname)
      @firstname = firstname
      @lastname = lastname
    end

    def fullname
      "#{@firstname} #{@lastname}"
    end
  end
end
