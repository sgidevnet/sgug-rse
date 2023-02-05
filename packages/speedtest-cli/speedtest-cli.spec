Name: speedtest-cli
Version: 2.1.1
Release: 3%{?dist}
Summary: Command line interface for testing internet bandwidth

License: ASL 2.0 
URL: https://github.com/sivel/speedtest-cli
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools

BuildArch: noarch

%description
Command line interface for testing internet bandwidth using speedtest.net

%prep
%autosetup
sed -i -e '/^#!\//, 1d' *.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 644 speedtest-cli.1 %{buildroot}%{_mandir}/man1/speedtest-cli.1
rm -f %{buildroot}%{_bindir}/speedtest

%files
%doc CONTRIBUTING.md README.rst
%license LICENSE
%exclude %{python3_sitelib}/__pycache__/
%{_bindir}/speedtest-cli
%{python3_sitelib}/speedtest_cli*
%{python3_sitelib}/speedtest.py
%{_mandir}/man1/speedtest-cli.1.*


%changelog
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Leigh Scott <leigh123linux@gmail.com> - 2.1.1-1
- Update to 2.1.1 release
- Remove pointless check, builders don't have internet access
- Use python3 macros
- Fix Source URL
- Remove gz extension from man file
- Don't bother compressing man file as rpmbuild does it
- Remove unnecessary Requires
- Spec file clean up

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Matias Kreder <delete@fedoraproject.org> - 1.0.2-1
- Updated to 1.0.2

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.3.2-8
- Rebuild for brp-python-bytecompile

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> - 0.3.2-3
- Switched to python

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> - 0.3.2-1
- Updated to 0.3.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Matias Kreder <delete@fedoraproject.org> 0.3.1-1
- Updated to 0.3.1, added python-setuptools as a dependency

* Mon Jul 14 2014 Matias Kreder <delete@fedoraproject.org> 0.3.0-1
- Initial spec

