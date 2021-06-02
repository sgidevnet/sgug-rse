Summary:    Script to colorize the compiler output
Name:       colorgcc
Version:    1.4.5
Release:    7%{?dist}
License:    GPL+
Url:        http://schlueters.de/colorgcc.html
Source0:    https://github.com/colorgcc/colorgcc/archive/%{version}.tar.gz
BuildArch:  noarch
Patch0:     colorgcc-invocation.patch
Patch1:     readme-fedora.patch
BuildRequires:     perl-generators
Requires:   perl-interpreter

%description
Perl script written by Jamie Moyers to colorize the terminal output of C++, CC,
CCACHE, G++, GCC so error messages can be found within longer compiler outputs. 

%prep
%setup
mv ./colorgccrc.txt ./colorgccrc.sample
%patch0 -p1
%patch1 -p1

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 colorgcc.pl $RPM_BUILD_ROOT/%{_bindir}/color-gcc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-g++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-cc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-c++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-ccache

ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorgcc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorg++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorcc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorc++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorccache

install -dm 755 $RPM_BUILD_ROOT%{_libdir}/colorgcc
for n in cc gcc g++ c++ ; do
    ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT%{_libdir}/colorgcc/$n
done

%files
%{_bindir}/color-gcc
%{_bindir}/color-g++
%{_bindir}/color-cc
%{_bindir}/color-c++
%{_bindir}/color-ccache

%{_bindir}/colorgcc
%{_bindir}/colorg++
%{_bindir}/colorcc
%{_bindir}/colorc++
%{_bindir}/colorccache

%dir %{_libdir}/colorgcc
%{_libdir}/colorgcc/*

%doc README colorgccrc.sample

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 8 2017 Martin Cermak <mcermak@redhat.com> 1.4.5-3
- Provide convenience symlinks per bz1402003#c10
- Update README

* Wed Dec 6 2017 Martin Cermak <mcermak@redhat.com> 1.4.5-1
- Rebase to 1.4.5 per bz1402003

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.3.2-16
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Martin Cermak <mcermak@redhat.com> 1.3.2-11
- Allow using "color" prefix as well as "color-" prefix (bz1078180)

* Fri Jan 03 2014 Martin Cermak <mcermak@redhat.com> 1.3.2-10
- Updated README

* Fri Jan 03 2014 Martin Cermak <mcermak@redhat.com> 1.3.2-9
- Renamed and updated config sample

* Thu Jan 02 2014 Martin Cermak <mcermak@redhat.com> 1.3.2-8
- Added README and sample config file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3.2-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May  4 2011 Martin Cermak <mcermak@redhat.com> 1.3.2-2
- Full URL for Source0 used
- License tag updated
- BuildRoot tag dropped
- Cleaned up the prep phase code
- Summary updated
- Compilers in the description updated and sorted alphabetically
- Absolute paths pointing to compiler binaries removed
- Resolves bz700833

* Fri Apr 29 2011 Martin Cermak <mcermak@redhat.com> 1.3.2-1
- Packaged for Fedora 

