Name:		python-pytest-harvest
Version:	1.7.2
Release:	3%{?dist}
Summary:	Store data created during test execution and retrieve it at the end

License:	BSD
URL:		https://pypi.org/project/pytest-harvest/
Source0:	%{pypi_source pytest-harvest}

Patch0:         0001-Fix-ResultsBag.__hash__-on-32-bit.patch

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

%description
Store data created during your pytest tests execution, and retrieve it
at the end of the session, e.g. for applicative benchmarking purposes.

%package -n python3-pytest-harvest
Summary: %{summary}
%{?python_provide:%python_provide python3-pytest-harvest}

%description -n python3-pytest-harvest
%{summary}.

%prep
%autosetup -n pytest-harvest-%{version} -p1

cat >pyproject.toml <<EOF
[build-system]
requires = ["pytest-runner",
	    "setuptools_scm",
            "wheel",
            "pandas",
            "tabulate",
	    "pypandoc",
	    "six"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

mv -i -v pytest_harvest/tests/conftest.py .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{__python3} -m pytest -v

%files -n python3-pytest-harvest
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_harvest/
%{python3_sitelib}/pytest_harvest-%{version}.dist-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.2-1
- Initial packaging
