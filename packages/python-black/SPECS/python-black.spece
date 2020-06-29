%global pypi_name        black
%global base_version     19.10
%global prerel           b0
%global upstream_version %{base_version}%{?prerel}
Name:           python-%{pypi_name}
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        3%{?dist}
Summary:        The uncompromising code formatter
License:        MIT
URL:            https://github.com/psf/black
Source0:        %{pypi_source %{pypi_name} %{upstream_version}}
Source1:        black.1
Source2:        blackd.1
# Tweak starred expression to work with Python 3.9 parser
# https://github.com/psf/black/pull/1477
Patch0:         0001-expression-tests-adjust-starred-expression-for-Pytho.patch
# FIXME: hack up beginning_backslash test to work around Python 3.9
# parser bug https://bugs.python.org/issue40847 . Not submitted
# upstream as this is just a hack, the new upstream Python parser
# needs to be fixed to not treat this as a syntax error
Patch1:         0001-HACK-nerf-beginning_backslash-test-to-pass-with-Pyth.patch
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.}

%description %_description


%package -n     %{pypi_name}
Summary:        %{summary}

# extras_require "d"
Recommends:     python3-aiohttp >= 3.3.2
Recommends:     python3-aiohttp-cors

# Package was renamed when Fedora 31 was rawhide
# Don't remove this before Fedora 33
Provides:       python3-%{pypi_name} = %{version}-%{release}
Obsoletes:      python3-%{pypi_name} < 19.4

%description -n %{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{upstream_version} -p1

%generate_buildrequires
# d is a name of extras_require
%pyproject_buildrequires -rx d


%build
%pyproject_wheel


%install
%pyproject_install

ln -s ./black %{buildroot}%{_bindir}/black-%{python3_version}
ln -s ./blackd %{buildroot}%{_bindir}/blackd-%{python3_version}
# ln -s ./black-{python3_version} {buildroot}{_bindir}/black-3

install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/black.1
install -D -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/blackd.1


%check
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
%{python3} setup.py test


%files -n %{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/black
%{_bindir}/black-%{python3_version}
%{_mandir}/man1/black.1*
%{_bindir}/blackd
%{_bindir}/blackd-%{python3_version}
%{_mandir}/man1/blackd.1*

%{python3_sitelib}/__pycache__/black*
%{python3_sitelib}/__pycache__/_black*
%{python3_sitelib}/black*.py
%{python3_sitelib}/_black*.py
%{python3_sitelib}/blib2to3/
%{python3_sitelib}/%{pypi_name}-%{upstream_version}.dist-info/


%changelog
* Wed Jun 03 2020 Adam Williamson <awilliam@redhat.com> - 19.10~b0-3
- Rebuilt for Python 3.9
- Fix one test and hack up another one for Python 3.9 parser issues

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10~b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Miro Hrončok <mhroncok@redhat.com> - 19.10~b0-1
- Update to 19.10b0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.3b0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-2
- Rename the binary package to black, rhbz#1692117

* Thu Mar 21 2019 Christian Heimes <cheimes@redhat.com> - 19.3b0-1
- New upstream release 19.3b0, rhbz#1688957

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.9b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Christian Heimes <cheimes@redhat.com> - 18.9b0-1
- New upstream version 18.9b0
- Include blackd daemon

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6b4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6b4-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Christian Heimes <cheimes@redhat.com> - 18.6b4-1
- New upstream release 18.6b4, rhbz#1593485
- Remove workaround for missing empty_pyproject.toml

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6b2-3
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Christian Heimes <cheimes@redhat.com> - 18.6b2-2
- Add new build and runtime dependency python3-toml
- Don't download external packages in tests
- Create missing empty_pyproject.toml for tests

* Sat Jun 09 2018 Christian Heimes <cheimes@redhat.com> - 18.6b2-1
- New upstream release 18.6b2, rhbz#1589399

* Wed Jun 06 2018 Christian Heimes <cheimes@redhat.com> - 18.6b1-1
- New upstream release 18.6b1

* Tue May 29 2018 Christian Heimes <cheimes@redhat.com> - 18.5b1-1
- New upstream release 18.5b0, rhbz#1579822

* Fri May 04 2018 Christian Heimes <cheimes@redhat.com> - 18.4a4-2
- Add man page
- Ignore false spelling warnings

* Wed May 02 2018 Christian Heimes <cheimes@redhat.com> - 18.4a4-1
- Initial package.
