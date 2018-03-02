require 'author'

describe 'Author' do
  it 'should return the fullname using first and last names' do
    author = Model::Author.new('Kent', 'Beck')
    expect(author.fullname).to eq('Kent Beck')
  end
end
