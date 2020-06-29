%global srcname twine

%bcond_without tests
%bcond_with internet

Name:           python-%{srcname}
Version:        3.2.0
Release:        1%{?dist}
Summary:        Collection of utilities for interacting with PyPI

License:        ASL 2.0
URL:            https://github.com/pypa/%{srcname}
Source0:        %{pypi_source}
# The dependencies for the docs pin Sphinx to a super old version
Source1:        twine.1
BuildArch:      noarch

%description
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.

%package -n %{srcname}
Summary:        Twine is a utility for publishing Python packages on PyPI

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(rfc3986)
BuildRequires:  python3dist(colorama)

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(portend)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(jaraco.envs)
BuildRequires:  python3dist(munch)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(requests-toolbelt)
BuildRequires:  python3dist(pkginfo)
BuildRequires:  python3dist(keyring)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(readme-renderer)
BuildRequires:  python3dist(pytest-cov)

%if %{with internet}
# pytest-services is not packaged yet
#BuildRequires:  python3dist(pytest-services)
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  git-core
%endif # with internet

%endif # with tests

Obsoletes:      python2-%{srcname} < 1.12.2-3
Obsoletes:      python3-%{srcname} < 1.12.2-3

%description -n %{srcname}
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{srcname}.1

%if %{with tests}
%check
%pytest -v \
%if %{without internet}
      --deselect tests/test_integration.py \
      --deselect tests/test_upload.py::test_check_status_code_for_wrong_repo_url \
%endif # without internet
;
%endif # with tests

%files -n %{srcname}
%license LICENSE
%doc README.rst AUTHORS
%{_mandir}/man1/%{srcname}.1*
%{_bindir}/twine
%{python3_sitelib}/twine/
%{python3_sitelib}/twine-*.egg-info/

%changelog
* Wed Jun 24 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.2.0-1
- Update to 3.2.0 (#1850277)

* Fri Jun 05 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.1.1-1
- Update to 3.1.1 (#1755042)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.15.0-1
- Update to 1.15.0 (#1750057).
- https://github.com/pypa/twine/blob/1.15.0/docs/changelog.rst

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Jeremy Cline <jcline@redhat.com> - 1.12.2-3
- Bump the obsoletes so the upgrade path from F29 works
- Include the manpage since the dep chain for docs building is broken

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.12.2-1
- Update to 1.12.2 (#1551178).
- https://github.com/pypa/twine/blob/1.12.2/docs/changelog.rst

* Tue Nov 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.10.0-6
- Drop python2 subpackage

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-5
- Make the keyring dependency optional
- Run tests

* Thu Sep 13 2018 Jeremy Cline <jeremy@jcline.org> - 1.10.0-4
- Update the summary of the "twine" package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Jeremy Cline <jeremy@jcline.org> - 1.10.0-1
- Update to latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Jeremy Cline <jeremy@jcline.org> - 1.9.1-4
- Re-add the Python 2 package (rhbz #1512552)

* Tue Oct 31 2017 Jeremy Cline <jeremy@jcline.org> - 1.9.1-3
- Drop pythonX- subpackages as Twine is a CLI (rhbz #1507815)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Jeremy Cline <jeremy@jcline.org> - 1.9.1-1
- Update to 1.9.1 (#1448841)
- Add python-keyring and python-tqdm as dependencies
- Remove python-clint as a dependency

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-2
- Rebuild for Python 3.6

* Tue Aug 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.8.1-1
- Update to 1.8.1

* Mon Jul 18 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-3
- Keep objects.inv to support intersphinx documentation

* Mon Jul 18 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-2
- Add clint as a build dependency so the tests pass

* Fri Jul 15 2016 Jeremy Cline <jeremy@jcline.org> - 1.7.4-1
- Update to the latest upstream release
- Add clint as a dependency

* Tue Jul 12 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-5
- Remove unnecessary shebang in __main__.py that caused rpmlint errors

* Mon Jul 11 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-4
- Mark man pages as docs

* Mon Jul 11 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-3
- Use python_version macro rather than hardcoding version numbers.

* Fri Jul 08 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-2
- Update Source0 url to the <name>-<version>.tar.gz format

* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-1
- Initial commit
