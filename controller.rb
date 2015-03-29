#app/controllers/jobs_controller.rb
class JobsController < ApplicationController
  ...

  def create
    @job = Job.new(job_params)
    @job.end_date = @job.start_date + 30.days

    if @job.save
      redirect_to @job, notice: 'Job was successfully created.'
    else
      render :new
    end
  end

  ...
end

### Notes:
# * Many actions in one class
# * The saving model and what params the model can take is handled directly in
#   this class
# * Readablity of 1.month is really nice
