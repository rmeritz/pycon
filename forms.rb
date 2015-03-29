# lib/validators/obscene_validator.rb
class ObseneValidator < ActiveModel::Validator
  def validate(record)
    if record.name.obscene?
      record.errors[:name] << 'No dirty names!'
    end
  end
end
