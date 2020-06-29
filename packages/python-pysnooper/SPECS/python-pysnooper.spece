Name:           python-pysnooper
Version:        0.2.5
Release:        4%{?dist}
Summary:        Poor man's debugger for Python

License:        MIT
URL:            https://github.com/cool-RR/pysnooper
Source0:        https://github.com/cool-RR/pysnooper/archive/%{version}/python-pysnooper-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
PySnooper is a replacement for debug print statements in code. After decorating
a function it automatically logs which lines were run and any changes to local
variables.}

%description %_description

%package -n python3-pysnooper
Summary:        %{summary}
%{?python_provides python3-pysnooper}

%description -n python3-pysnooper %_description

%prep
%autosetup -n PySnooper-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %__python3 -m pytest -v tests/

%files -n python3-pysnooper
%license LICENSE
%doc README.md
%{python3_sitelib}/pysnooper/
%{python3_sitelib}/PySnooper-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.5-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.2-1
- Update to latest version

* Sat Jun 15 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-1
- Initial packaging
