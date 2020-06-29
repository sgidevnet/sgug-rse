%{?python_enable_dependency_generator}
%global modname aiofiles

Name:           python-%{modname}
Version:        0.4.0
Release:        8%{?dist}
Summary:        File support for asyncio

License:        ASL 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
aiofiles is an Apache2 licensed library, written in Python, for handling\
local disk files in asyncio applications.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Enable python dependency generator

* Mon Sep 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
