Summary: Ncurses based hexadecimal editor with a diff mode
Name: dhex
Version: 0.69
Release: 2%{?dist}
License: GPLv2+
URL: http://www.dettus.net/dhex/
Source: http://www.dettus.net/dhex/%{name}_%{version}.tar.gz
Patch0: dhex-0.69-build-fix.patch
BuildRequires: gcc, ncurses-devel

%description
DHEX is a more than just another hex editor: It includes a diff mode, which
can be used to easily and conveniently compare two binary files. Since it is
based on ncurses and is themeable, it can run on any number of systems and
scenarios. With its utilization of search logs, it is possible to track
changes in different iterations of files easily.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .build-fix

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" %{?__global_ldflags: LDFLAGS="%{__global_ldflags}"}

%install
install -dD %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man{1,5}
make %{?_smp_mflags} DESTDIR=%{buildroot} BINDIR=%{_bindir} \
     MANDIR=%{_mandir} install

%files
%doc README.txt gpl.txt todo.txt

%{_bindir}/*
%{_mandir}/*/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb  5 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.69-1
- New version
  Resolves: rhbz#1667679

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.68-11
- Fixed FTBFS by adding gcc requirement

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.68-2
- Various fixes according to review

* Fri Jun 20 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.68-1
- Initial release
