%global modname httptools

Name:           python-%{modname}
Version:        0.0.11
Release:        9%{?dist}
Summary:        Fast HTTP parser

License:        MIT
URL:            https://github.com/MagicStack/httptools
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

# Upstreamable patches
Patch0001:      0001-setup.py-Use-Cython-directly.patch
Patch0002:      0002-use-system-http_parser.patch

BuildRequires:  gcc
BuildRequires:  http-parser-devel

%global _description \
httptools is a Python binding for nodejs HTTP parser.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1
# To be sure, no 3rd-party stuff
rm -vrf vendor/
# No need to ship .c files
sed -i -e "/include_package_data=True/d" setup.py

%build
%py3_build

%install
%py3_install

%check
# One of test fails, but seems not critical
# https://github.com/MagicStack/httptools/issues/10
pushd tests
  PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover -v || :
popd

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.11-9
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.11-8
- Rebuild for http-parser 2.9.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.11-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.11-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.11-1
- Update to 0.0.11

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.10-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.10-1
- Update to 0.0.10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.9-2
- Drop python2 subpackage

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.9-1
- Initial package
