Name:           tfdocgen
Version:        20150202git
Release:        11%{?dist}
Summary:        TiLP framework documentation generator

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/

#To get source archive, run the following commands:
# git clone git://tilp.git.sourceforge.net/gitroot/tilp/tfdocgen/ SNAPSHOT_DATE
# tar cfj tfdocgen-SNAPSHOT_DATE.tar.bz2 tfdocgen-SNAPSHOT_DATE/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  glib2-devel

%description
The tfdocgen program is a program used by the libti*
libraries to generate their HTML documentation from
sources and misc files. You don't need this package
unless you want to develop on the libti*2 libraries.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/tfdocgen
%{_mandir}/man1/tfdocgen.1.*
%license COPYING
%doc README AUTHORS ChangeLog

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150202git-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150202git-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 9 2015 'Ben Rosser' <rosser.bjr@gmail.com> 20150202git-2
- Added license tag, added an extra file to doc.
- Changed tfdocgen man page to use a wildcard encoding.

* Mon Feb 2 2015 'Ben Rosser' <rosser.bjr@gmail.com> 20150202git-1
- Bumped changelog and checkout date.

* Fri Oct 11 2013 'Ben Rosser' <rosser.bjr@gmail.com> 20131011git-1
- Updated to latest checkout from git repository

* Wed Jul 11 2012 'Ben Rosser' <rosser.bjr@gmail.com> 20120711git-1
- Initial version of the package
