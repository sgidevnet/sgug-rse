Name:    dmenu
Version: 5.0
Release: 0
Summary: dmenu is an efficient dynamic menu for X. 

License: MIT
URL:     https://tools.suckless.org/dmenu/
Source0: https://dl.suckless.org/tools/dmenu-5.0.tar.gz

Patch100: dmenu.sgifixes.patch


%description
Initial 


%prep
%autosetup -p1

%build
make

%install
%make_install


%files
%{_bindir}/dmenu
%{_bindir}/dmenu_path
%{_bindir}/dmenu_run
%{_bindir}/stest
%{_mandir}/man1/dmenu*
%{_mandir}/man1/stest*

%changelog
* Sat Jan 1 2022 Eric Dodd <eric.e.dodd@gmail.com> - 5.0-0
- Initial package
