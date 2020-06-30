# Created by pyp2rpm-3.2.1
%global srcname ndjson-testrunner
%global srcname_ ndjson_testrunner

Name:           python-%{srcname}
Version:        1.0.0
Release:        10%{?dist}
Summary:        A test runner that outputs newline delimited JSON results

License:        GPLv3+
URL:            https://github.com/flying-sheep/ndjson-testrunner
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
# https://github.com/flying-sheep/ndjson-testrunner/pull/1
Source1:        COPYING
Source2:        tests.py

BuildArch:      noarch

%global _description \
A unittest TestRunner that outputs ndjson, one JSON record per test result. To \
be used for test result storage or interprocess communication.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
cp -p %SOURCE1 %SOURCE2 .

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install


%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    %{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.rst
%license COPYING
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname_}.py
%{python3_sitelib}/%{srcname_}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Initial package.
