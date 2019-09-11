#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ninja
Version  : 1.9.0
Release  : 9
URL      : https://github.com/ninja-build/ninja/archive/v1.9.0.tar.gz
Source0  : https://github.com/ninja-build/ninja/archive/v1.9.0.tar.gz
Summary  : Ninja is a small build system with a focus on speed.
Group    : Development/Tools
License  : Apache-2.0
Requires: ninja-bin = %{version}-%{release}
Requires: ninja-license = %{version}-%{release}

%description
Ninja is yet another build system. It takes as input the interdependencies of files (typically source code and output executables) and
orchestrates building them, quickly.

Ninja joins a sea of other build systems. Its distinguishing goal is to be fast. It is born from my work on the Chromium browser project,
which has over 30,000 source files and whose other build systems (including one built from custom non-recursive Makefiles) can take ten
seconds to start building after changing one file. Ninja is under a second.

%package bin
Summary: bin components for the ninja package.
Group: Binaries
Requires: ninja-license = %{version}-%{release}

%description bin
bin components for the ninja package.


%package license
Summary: license components for the ninja package.
Group: Default

%description license
license components for the ninja package.


%prep
%setup -q -n ninja-1.9.0

%build
## build_prepend content
python3 configure.py --bootstrap --verbose
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568218857
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} ||:


%install
export SOURCE_DATE_EPOCH=1568218857
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ninja
cp COPYING %{buildroot}/usr/share/package-licenses/ninja/COPYING
%make_install ||:
## install_append content
install -Dpm0755 ninja -t %{buildroot}/usr/bin/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ninja

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ninja/COPYING
