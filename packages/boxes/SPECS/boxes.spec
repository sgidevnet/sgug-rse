# The GNU C Library no longer implements <regexp.h> #67
# * https://github.com/ascii-boxes/boxes/issues/67
%global debug_package %{nil}

%global cfgfile %{_datadir}/%{name}/%{name}

Name:           boxes
Version:        1.3
Release:        3%{?dist}
Summary:        Draw any kind of box around some given text

License:        GPLv2+
URL:            http://boxes.thomasjensen.com
Source0:        https://github.com/ascii-%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
Recommends:     %{name}-vim = %{version}-%{release}

%description
"boxes" is a text filter which can draw ASCII art boxes around its input text.
These boxes may also be removed, even if they have been badly damaged by editing
of the text inside. Since boxes may be open on any side, boxes can also be used
to create regional comments in any programming language. With the help of an
editor macro or mapping, damaged boxes can easily be repaired. This is useful
for making the function headers in your programming language look better, for
spicing up your news postings and emails, or just for decorating your
documentation files. New box designs of all sorts can easily be added and shared
by appending to a free format configuration file. boxes was intended to be used
with the vim text editor, but can be tied to any text editor which supports
filters.


%package        vim
BuildArch:      noarch

Summary:        Vim plugin for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       vim-enhanced

%description    vim
Vim plugin for %{name}.


%prep
%autosetup -p1


%build
%set_build_flags
%make_build                     \
    GLOBALCONF=%{cfgfile}       \
#   CFLAGS='%{optflags}'        \
#   LDFLAGS='%{build_ldflags}'  \
#   STRIP=false


%check
%make_build test


%install
install -Dp -m 0755 src/%{name}     %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}-config  %{buildroot}%{cfgfile}
install -Dp -m 0644 doc/%{name}.1   %{buildroot}%{_mandir}/man1/%{name}.1
install -Dp -m 0644 %{name}.vim     %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/*

%files vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim


%changelog
* Thu Jan 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3-3
- Packaging fixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3-1
- Update to 1.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Jakub Hrozek <jhrozek@redhat.com> - 1.1.1-13
- BuildRequire gcc
- rhbz #1603515 - boxes: FTBFS in Fedora rawhide

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.1-4
- Fix race condition in parallel make (#1106015)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.1.1-2
- Fix -Wformat-security compilation warning

* Wed Jul 31 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.1.1-1
- New upstream release 1.1.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Jakub Hrozek <jhrozek@redhat.com> - 1.1-6
- bump release

* Sun Feb 10 2008 Jakub Hrozek <jhrozek@redhat.com> - 1.1-5
- rebuild for GCC 4.3

* Wed Jan 09 2008 Jakub Hrozek <jhrozek@redhat.com> - 1.1-4
- fix the license tag from GPL2 to GPL2+

* Sat Oct 13 2007 Jakub Hrozek <jhrozek@redhat.com> - 1.1-3
- More packaging fixes spotted in review (292121), especially:
- remove slashes between macros and buildroot
- set default permissions for directories in defattr
- fix whitespace change in the patch, rename for clarity
- drop the emacs helper

* Sun Sep 30 2007 Jakub Hrozek <jhrozek@redhat.com> - 1.1-2
- Fix packaging mistakes spotted in the review request, namely:
- patch makefile so that optflags are passed
- use macro for the boxfile location as it's used frequently
- fix rpmlint
- package emacs helper

* Sat Sep 15 2007 Jakub Hrozek <jhrozek@redhat.com> - 1.1-1
- initial packaging
