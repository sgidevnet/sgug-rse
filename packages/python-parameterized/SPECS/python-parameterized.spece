%global srcname parameterized

Name:           python-%{srcname}
Version:        0.7.0
Release:        3%{?dist}
Summary:        Parameterized testing with any Python test framework

License:        BSD
URL:            https://pypi.python.org/pypi/parameterized
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

# Python 3.8
Patch0:         https://github.com/wolever/parameterized/pull/75/commits/1842e2038ae123e16601e083a553fe931f34fbd0.patch

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-nose2
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
sed -i 's|^import mock|from unittest import mock|' parameterized/test.py
export PYTHONPATH=%{buildroot}%{python3_sitelib}
nosetests-%{python3_version} -v
nose2-%{python3_version} -v
py.test-%{python3_version} -v parameterized/test.py
%{__python3} -m unittest -v parameterized.test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGELOG.txt README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Jiri Popelka <jpopelka@redhat.com> - 0.7.0-1
- 0.7.0
- Don't use now orphaned python-unittest2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-5
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Initial package
