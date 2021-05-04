Name:           prename
Version:        1.9
Release:        8%{?dist}
Summary:        Perl script to rename multiple files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/rename
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEDERST/rename-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pstray/rename/master/LICENSE

# This patch renames the executable from rename to prename
Patch0:         %{name}-1.9-namechange.patch
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)


%description
Prename renames the file names supplied according to the rule specified as
the first argument. The argument is a Perl expression which is expected
to modify the $_ string for at least some of the file names specified.


%prep
%autosetup -p1 -n rename-%{version}
cp %{SOURCE1} .

%build
%__perl Makefile.PL PREFIX=%{_prefix} NO_PACKLIST=1
%make_build


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.9-4
- Added LICENSE from upstream

* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.9-3
- Fix for Fedora Review

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.9-2
- Update to Fedora Packaging Guidelines specification

* Mon Oct 17 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.9-1
- Initial release
