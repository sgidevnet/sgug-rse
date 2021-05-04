%{?python_enable_dependency_generator}

Name:           gcovr
Version:        4.1
Release:        4%{?dist}
Summary:        A code coverage report generator using GNU gcov

License:        BSD
URL:            http://gcovr.com/
Source0:        https://github.com/gcovr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       %{_bindir}/gcov

BuildArch:      noarch

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This command is inspired by the Python coverage.py package, which provides
a similar utility in Python. The gcovr command produces either compact
human-readable summary reports, machine readable XML reports
(in Cobertura format) or simple HTML reports. Thus, gcovr can be viewed
as a command-line alternative to the lcov utility, which runs gcov and
generates an HTML-formatted report.


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%files
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/gcovr
%{python3_sitelib}/gcovr*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Neal Gompa <ngompa13@gmail.com> - 4.1-2
- Add missing files installed in the Python sitelib location

* Fri Sep 07 2018 Neal Gompa <ngompa13@gmail.com> - 4.1-1
- Release 4.1 to Fedora (#1626452)
- Reformatted changelog entry

* Fri Sep 07 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 4.1-0
- Update to latest gcovr version (4.1)
- Removed backported upstream patch as it is part of the release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-4
- Fix HTML reports for Python 3 (#1428277)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-2
- Address review comments (#1418804)
- Switch to Python 3


* Thu Feb  2 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-1
- Initial package
