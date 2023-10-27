subroutine Folder_output (k, istep, foldername, produce_output)


    use FastScapeContext
    implicit none

    integer, intent(in) :: k, istep
    character(len=k), intent(in) :: foldername
    integer, intent(in) :: produce_output


    ffoldername = foldername
    kk = k
    iistep = istep
    produce_output_now = .false.
    if (produce_output.eq.1) produce_output_now = .true.


    return
  end subroutine Folder_output
