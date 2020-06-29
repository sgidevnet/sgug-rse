%global srcname mpd2

Name:           python-%{srcname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Python library providing a client interface for MPD

License:        LGPLv3+
URL:            https://github.com/Mic92/python-mpd2
Source0:        https://github.com/Mic92/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{_bindir}/tox

%description
Python library providing a client interface for MPD.

%package -n python3-%{srcname}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-coverage
BuildRequires:  python3-mock
BuildRequires:  python3-twisted
Summary:        Python 3 mpd2 module
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python3 library providing a client interface for MPD.


%package doc
Summary:    Documentation for %{name}
BuildRequires:  python3-sphinx

%description doc
This package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}
rm -frv %{srcname}.egg-info

# Use coverage3 instead of coverage
# space is important
sed -i 's/coverage /coverage3 /' tox.ini

%build
%py3_build

pushd doc
    make html
    find . -name ".buildinfo" -exec rm -f '{}' \;
popd

%install
%py3_install

%check
TOX_TESTENV_PASSENV=PYTHONPATH TOXENV=py%{python3_version_nodots} tox --sitepackages

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/*%{srcname}-%{version}-py3.?.egg-info/
%{python3_sitelib}/mpd

%files doc
%doc doc/_build/html


%changelog
* Sat Jun 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-1
- Update to 1.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-1
- Update to latest release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.5-11
- Subpackage python2-mpd2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.5-10
- Correct macro

* Fri Jul 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.5-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-7
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-6
- BuildRequire and invoke tox directly (allows us to drop python2-tox from the distro)
- Use macro instead of hardcoded Python 3.6 version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.5-4
- Use versioned python build requires

* Sat Oct 28 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.5-3
- Use git tags instead of commit info

* Sat Oct 28 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.5-2
- Changes based on suggestions in review ticket #1507235
- Improve summary
- Add tests
- Redo release string

* Sun Aug 21 2016 Kushal Das <kushal@fedoraproject.org> 0.5.5-1
- Initial package
