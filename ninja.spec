#
Name     : ninja
Version  : 1.8.2
Release  : 6
URL      : https://github.com/ninja-build/ninja/archive/v1.8.2.tar.gz
Source0  : https://github.com/ninja-build/ninja/archive/v1.8.2.tar.gz
Summary  : Ninja is a small build system with a focus on speed
Group    : Development/Tools
License  : Apache-2.0
Requires: scikit-build
BuildRequires : cmake
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : scikit-build
BuildRequires : setuptools

%description
Ninja Python Distributions
        ==========================

%prep
%setup -q -n ninja-1.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500401369
python3 configure.py --bootstrap --verbose


%install
rm -rf %{buildroot}
install -Dpm0755 ninja -t %{buildroot}%{_bindir}/


%files
%defattr(-,root,root,-)
/usr/bin/ninja
